const _ = require('lodash');

const numbers = [33,46,76,44,32,37,84];

_.each(numbers, function(number, i) {

    console.log(number);
});