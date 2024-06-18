#!/usr/bin/node
const num = Number(process.argv[2]);
function fact(num) {
	if (isNaN(num)) {
		return (1);
	} else {
		if (num == 0) {
			return (1);
		} else {
			return (num * fact(num - 1));
		}
	}
}
