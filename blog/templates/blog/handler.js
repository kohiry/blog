
let post__containers = document.querySelectorAll(".post-container")

window.onload = () => {
	for(let i = 0; i < post__containers.length; i++) {
		let post     = post__containers[i].querySelector(".post")
		let comments = post__containers[i].querySelector(".comments")

		let mail__wrappers    = post__containers[i].querySelectorAll(".mail-wrapper")
		let post__preview     = post__containers[i].querySelector(".post-preview")
		let comments__preview = post__containers[i].querySelector(".comments-preview")
		let likes__counter	  = post.querySelector(".likes-counter")

		let like__btn  = post.querySelector(".like-btn")
		let post__btns = post__containers[i].querySelectorAll(".unwrap-btn")

		post.dataset.height     = post.clientHeight
		comments.dataset.height = comments.clientHeight

		post.dataset.opened     = "false"
		comments.dataset.opened = "false"

		post.classList.toggle("wrap")
		comments.classList.toggle("wrap")

		// Buttons event controls 
		post__btns[0].onclick = () => {
			post__btns[0].querySelector("i").classList.toggle("rotate")

			if(post.dataset.opened == "false") {
				post.dataset.opened = "true"
				post.style.setProperty("max-height", `${post.dataset.height}px`)
				post__preview.style.setProperty("border-radius", "15px 15px 0 0")
				let post__timeout = setTimeout(() => {
					post.classList.toggle("wrap")
					clearTimeout(post__timeout)
				}, 500)
			} else {
				post.dataset.opened = "false"
				post.classList.toggle("wrap")
				post.style = "border-radius: 0 0 15px 15px; max-height: 0px"
				let post__timeout = setTimeout(() => {
					post.style = "border-radius: 0 0 15px 15px;"
					post__preview.style = "border-radius: 15px;"
					clearTimeout(post__timeout)
				}, 460)
			}
		}

		post__btns[1].onclick = () => {
			post__btns[1].querySelector("i").classList.toggle("rotate")

			if(comments.dataset.opened == "false") {
				comments.dataset.opened = "true"
				comments.style.setProperty("max-height", `${post.dataset.height}px`)
				comments__preview.style.setProperty("border-radius", "0")
				let comments__timeout = setTimeout(() => {
					comments.classList.toggle("wrap")
					clearTimeout(comments__timeout)
				}, 500)
			} else {
				comments.dataset.opened = "false"
				comments.classList.toggle("wrap")
				comments.style = "border-radius: 0 0 15px 15px; max-height: 0px"
				let comments__timeout = setTimeout(() => {
					comments.style = "border-radius: 0 0 15px 15px;"
					comments__preview.style = "border-radius: 0 0 15px 15px;"
					clearTimeout(comments__timeout)
				}, 460)
			}
		}

		like__btn.onclick = () => {
			// likes__counter.dataset.likes = parseInt(likes__counter.dataset.likes) + 1
			likes__counter.textContent = likes__counter.dataset.likes
			if(parseInt(likes__counter.dataset.likes) >= 1000) {
				likes__counter.textContent = likes__counter.textContent[0] + "K"
			}
		}

		if(post__preview.querySelector(".post-title").textContent.length >= 46) {
			post__preview.querySelector(".post-title").style.setProperty("font-size", "24px")
		}

		mail__wrappers.forEach((mail__wrapper) => {
			let user__mail = mail__wrapper.querySelector(".user-mail")
			user__mail.onclick = () => {
				navigator.clipboard.writeText(user__mail.textContent)
				mail__wrapper.querySelector(".pop-up__copied").style = "opacity: 1"
				let pop__up_timeout = setTimeout(() => {
					mail__wrapper.querySelector(".pop-up__copied").style = "opacity: 0"
					clearTimeout(pop__up_timeout)
				}, 1000)
			}
		})
	}
}