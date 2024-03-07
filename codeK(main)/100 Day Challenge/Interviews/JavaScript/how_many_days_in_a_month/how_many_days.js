const how_many_days = (month) => {
  // user switch statement to check the month and return the number of days
  switch (month) {
    case 1 || 3 || 5 || 7 || 8 || 10 || 12:
      return 31;
    case 4 || 6 || 9 || 11:
      return 30;
    case 2:
      return 28;
    default:
      return "Invalid";
  }
};

// Test the function
const result = how_many_days(2);
console.log(result);
