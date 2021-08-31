//  TASK 1

function getMin(arr) {
    return Math.min.apply(Math, arr)
  //  arr.sort();
  //  arr.join(', ');
  //  arr.sort((a, b) => a-b);
  //  return arr[0]
}

//  TASK 2



//  TASK 3

const Checker = require('./Checker.js');

class Movie {

    constructor(name, category, startShow) {
        this.name = name;
        this.category = category;
        this.startShow = startShow;
    }

    watchMovie() {
        return "I watch the movie " + this.name + "!";
    }

}

const movie1 = new Movie('Titanic', 'drama', 1997);
const movie2 = new Movie('Troya', 'historical', 2004);


//  TASK 4

const Checker = require('./Checker.js');

class Student {

    constructor(fullName, direction) {
      this._fullName = fullName;
      this._direction = direction;
    }

    showFullName() {
        return this._fullName;
    }

    nameIncludes(data) {
        return this._fullName.includes(data) ? 'true' : 'false';
    }

    static StudentBuilder(fullName, direction) {
        return new Student(fullName, direction);
    }

    get direction() {
        return this._direction;
    }

    set direction(direction) {
        this._direction = direction;
    }
}

const stud1 = new Student('Ivan Petrenko', 'web');
const stud2 = new Student('Sergiy Koval', 'python');
const stud3 = new Student('Ihor Kohut', 'qc');


//  TASK 5

function mapCreator(keys, values) {
   const map = new Map();
   for(let i = 0; i < keys.length; i++) {
       if (typeof values[i] === 'string') {
           map.set(keys[i], values[i]);
       }
   }
   return map;
}