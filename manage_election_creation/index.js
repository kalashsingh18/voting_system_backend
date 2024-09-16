function countDesktopProducts(numOfProducts, productIDs) {
    // Define the set of laptop product IDs
    const laptopIDs = new Set(['a', 'l', 'e', 'o', 'u', 'A', 'I', 'E', 'O', 'U']);
    
    // Initialize the count for desktop products
    let desktopCount = 0;
    
    // Iterate through each product ID
    for (const productID of productIDs) {
        // Check if the product ID is not in the laptopIDs set
        if (!laptopIDs.has(productID)) {
            desktopCount++;
        }
    }
    
    // Print the result
    console.log(desktopCount);
}

// Example Usage
const numOfProducts = parseInt(prompt().trim(), 10);
const productIDs = prompt().trim().split(' ');
countDesktopProducts(numOfProducts, productIDs);