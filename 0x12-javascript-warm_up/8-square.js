#!/usr/bin/node
const num = Number(process.argv[2])
if (isNaN(num)) {
	console.log('Missing size')
} else {
	let hashtag = "";
	for (let i = 0; i < num; i++) {
		for (let j = 0; j < num; j++) {
			hashtag += "#";
		}
		console.log(hashtag);
		hashtag = "";
	}
}
