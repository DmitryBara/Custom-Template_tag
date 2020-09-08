// Call this js if page with menu just loading on default
// If page don't need to have pre-opened items


// console.log('MenuId const array: ', menuId)

window.onload = function() {

	for (id of menuId) {

		toggler = document.getElementsByClassName("caret " + id)

		for (var i = 0; i < toggler.length; i++) {

			toggler[i].addEventListener("click", function() {
			  	this.parentElement.querySelector(".nested").classList.toggle("active");
			  	this.classList.toggle("caret-down");
			} );
		}
	}
}