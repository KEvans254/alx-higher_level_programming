#!/usr/bin/node
function factorial (num) {
  let fact = 1;
  if (num !== NaN) {
    for (let i = 1; i <= num; i++) {
      fact *= i;
    }
  }
  console.log(fact);
}
factorial(parseInt(process.argv[2]));
