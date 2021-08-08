// function max(numbers) {
//   // your code here, for-loop method preferred
//   max_number = numbers[0];
//   var i;
//   for (i = 0; i < numbers.length; i++) {
//     if (numbers[i] >= max_number) {
//       max_number = numbers[i];
//     }
//   }
//   return max_number;
// }
// console.log(max([1, 2, 4, 5])); // should print 5
// console.log(max([5, 2, 7, 1, 6])); // should print 7

// console.log(
//   "-------------------------------------------------------------------------------------------------"
// );

function findPosition(numbers, target) {
  // your code here, for-loop method preferred
  var position_number = 0;
  var check_number = -1;
  for (var i = 0; i < numbers.length; i++) {
    if (position_number + 1 == numbers.length) {
      return check_number;
    }
    if (numbers[i] == target) {
      return position_number;
      break;
    } else if (numbers[i] != target) {
      if (position_number + 1 < numbers.length) {
        position_number += 1;
        // console.log("position_number:" + position_number);
      }
    }
  }
}

console.log(findPosition([5, 2, 7, 1, 6], 5)); // should print 0
console.log(findPosition([5, 2, 7, 1, 6], 7)); // should print 2
console.log(findPosition([5, 2, 7, 7, 7, 1, 6], 7)); // should print 2 (the first one)
console.log(findPosition([5, 2, 7, 1, 6], 8)); // should print -1
