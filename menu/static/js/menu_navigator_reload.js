// Call this js if page with menu have pre-opened menu items


// From element path create array of all parents of current element, include itself
splitted = curElementPath.split('.')


var way = ''
var parents = []

for (i = 0; i < splitted.length; i++) {
	if (way == '') {
		way = splitted[i]
	} else {
		way = way + '.' + splitted[i] 
	}
	parents.push(way)
}

parents.shift()

// Logic witch open elements in menu
for (path of parents) {
	knot = document.getElementById(path)

	try {
		knot.querySelector(".nested").classList.toggle("active")
		knot = null
	} catch {}

	try {
		knot.parentElement.querySelector(".nested").classList.toggle("active")
		knot.classList.toggle("caret-down")
	} catch {}
}


