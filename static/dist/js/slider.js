function initSlider(){
    const slider = document.querySelector(".items-slider");
		const slides = document.querySelectorAll(".item-slider");
		const button = document.querySelectorAll(".button-slider");

		let current = 1;
		let prev = 0;
		let next = 2;

		for (let i = 0; i < button.length; i++) {
			button[i].addEventListener("click", () => i == 0 ? gotoPrev() : gotoNext());
		}

		const gotoPrev = () => current > 0 ? gotoNum(current - 1) : gotoNum(slides.length - 1);

		const gotoNext = () => current < slides.length - 1 ? gotoNum(current + 1) : gotoNum(0);

		const gotoNum = number => {
			current = number;
			prev = current - 1;
			next = current + 1;

			for (let i = 0; i < slides.length; i++) {
				slides[i].classList.remove("active");
				slides[i].classList.remove("prev");
				slides[i].classList.remove("next");
			}

			if (next === slides.length) {
				next = 0;
			}

			if (prev === -1) {
				prev = slides.length - 1;
			}

			slides[current].classList.add("active");
			slides[prev].classList.add("prev");
			slides[next].classList.add("next");
		}
}
initSlider()