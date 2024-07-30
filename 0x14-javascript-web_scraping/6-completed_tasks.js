#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
const user = {
};
request.get(url, { json: true }, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    for (const todo of body) {
      if (todo.completed === true) {
        if (todo.userId in user) {
          user[todo.userId] += 1;
        } else {
          Object.assign(user, { [todo.userId]: 1 });
        }
      }
    }
    console.log(user);
  }
}
);
