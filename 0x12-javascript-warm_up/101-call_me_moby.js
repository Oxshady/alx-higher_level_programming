#!/usr/bin/node

function callMeMoby (x, theFunction) {
  let i = 0;

  while (i < x) {
    i++;
    theFunction();
  }
}
module.exports = {
  callMeMoby
};
