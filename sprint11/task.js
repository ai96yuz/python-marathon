// TASK 1


const filterNums = (arr, val, condition) => {
  var result = [];
  for (let i = 0; i < arr.length; i = i + 1) {
    if (val !== undefined) {
      if (condition === undefined || condition == "greater") {
        if (arr[i] > val) {
          result.push(arr[i]);
        }
      } else if (condition == "less") {
        if (arr[i] < val) {
          result.push(arr[i]);
        }
      }
    } else {
      if (arr[i] > 0) {
        result.push(arr[i]);
      }
    }
  }
  return result;
};


// TASK 2


const howMuchSec = (sec = 0, min = 0, hour = 0, day = 0, week = 0, month = 0, year = 0) => {
    return sec + min * 60 + hour * 3600 + day * 86400 + week * (86400 * 7) + month * (86400 * 30) + year * (86400 * 360);
};


// TASK 3


const maxInterv = (...arr) => {
    return arr.slice(1).reduce(function (prev, current, index) {
        return Math.max(Math.abs(arr[index] - current), prev);
    }, 0);
    // return Math.max(...Array(arr.length-1).fill().map((_,i) => Math.abs(arr[i]-arr[i+1])), 0);
}


// TASK 4


const sumOfLen = (...arr) => {
    return arr.map(w => w.length).reduce((total, amount) => total + amount, 0);
}