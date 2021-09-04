//  TASK 1


function getMin(arr) {
    return Math.min.apply(Math, arr)
}


//  TASK 2


const product = function() {
    return [].reduce.call(arguments, function(res, elem) {
        return res * elem;
    }, this.product);
};

const contextObj = {
    product: 10
}

const getProduct = product.bind(contextObj, 2, 3)


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
        const spliter = this.showFullName().split()
        return spliter[0].includes(data) ? 'true' : 'false';
    }

    static studentBuilder(fullName, direction) {
        return new Student('Ihor Kohut', 'qc');
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
const stud3 = Student.studentBuilder();


//  TASK 5


function mapCreator(keys, values) {
   const map = new Map();
   if (keys.length == values.length){
       values.filter(elem => typeof elem == 'string').forEach(element => map.set(keys[values.indexOf(element)], element));
        return map;
   }
}