#!/usr/bin/node

function factorial (a) {
  if (a <= 0) {
    return 0;
  } else if (a === 1) {
    return 1;
  } else {
    return (a * factorial(a - 1));
  }
}

const myInt = parseInt(process.argv[2]);
if (isNaN(myInt)) {
  console.log('1');
} else {
  console.log(factorial(myInt));
}
