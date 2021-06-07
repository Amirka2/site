const elements = document.querySelectorAll('.num');
Array.from(elements).forEach((el)=> el.addEventListener('click', (e) => {
	e.currentTarget.classList.toggle('active')
}))