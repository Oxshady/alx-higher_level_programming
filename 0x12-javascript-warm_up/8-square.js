#!/usr/bin/node
const num = Number(process.argv[2])
if (isNaN(num)) {
	console.log('Missing size')
} else {
	let sym = "";
	for (let i = 0; i < num; i++) {
		for (let j = 0; j < num; j++) {
			sym += "X";
		}
		console.log(sym);
		sym = "";
	}
}
