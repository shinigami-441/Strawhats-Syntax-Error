// Parse the current URL to get the search parameters
const urlSearchParams = new URLSearchParams(window.location.search);

// Get the value of the 'code' parameter
const idToken = urlSearchParams.get('code');
console.log(idToken);
// const userAttributes = JSON.parse(atob(idToken.split('.')[1]));
// console.log(userAttributes);

