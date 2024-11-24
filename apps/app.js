// Function to get a random number between min and max (inclusive)
const getRandomNumber = (min, max) => {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Function to handle the generation of the random number when the button is clicked
const generate = () => {
    const minEl = document.getElementById('min');
    const maxEl = document.getElementById('max');

    const min = Number(minEl.value);
    const max = Number(maxEl.value);

    // Check if the user has entered valid values for min and max
    if (minEl.value === '' || maxEl.value === '') {
        alert("Iltimos, min va max qiymatlarini kiriting!");
        return;
    }

    if (min > max) {
        alert("Min qiymat max qiymatidan kichik bo'lishi kerak!");
        return;
    }

    // Update the placeholder with the random number
    const placeholderEl = document.querySelector('#placeholder');
    placeholderEl.textContent = getRandomNumber(min, max);
}

// Attach the event listener to the button
const btnEl = document.getElementById('generate');
btnEl.addEventListener('click', generate);
