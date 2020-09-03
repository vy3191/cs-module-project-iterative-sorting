// Add up and print the sum of the all of the minimum elements of each inner 
const arr = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
// The expected output is given by:4 + -1 + 9 + -56 + 201 + 18 = 175
// You may use whatever programming language you’d like.
// Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.




// 1). write a function that can handle this problems
// 2). Inside the function, loop through the array starting from 0 index to last index of the array.
// 3)  for each inner array, compare the the elements and return the smallest element.
// 4. each smallest element from the inner array needs to summed up in the first iterative.
// 5). Return the total or sum

function Sum(arr) {
  if ( typeof arr !== 'array' && length(arr)===0) return "Please pass a valid array with elements";
  let sum = 0;
  for(let i=0; i<arr.length; i++) {
       const insideArr = arr[i];
       let min;
       for(let j =0; j < insideArr.length; j++) {
           min = insideArr[j];
           if(min > insideArr[j]) {
              min = insideArr[j]
           }          
       }
       sum += min
  }
  return sum;
}

Sum(arr)