// Get the list container
const listContainer = document.querySelector('.list-item');
const listContainercopy = document.querySelector('.list-item');

// Function to sort the list by name
function sortByName() {
  const items = Array.from(listContainer.querySelectorAll('.data-item'));

  items.sort((a, b) => {
    const nameA = a.querySelector('.itemtitle').textContent;
    const nameB = b.querySelector('.itemtitle').textContent;
    return nameA.localeCompare(nameB);
  });

  // Clear existing items
  listContainer.innerHTML = '';

  // Append sorted items
  items.forEach(item => listContainer.appendChild(item));
}

// Function to sort the list by date_added
function sortByDateAdded() {
  const items = Array.from(listContainer.querySelectorAll('.data-item'));

  items.sort((a, b) => {
    const dateAddedA = new Date(a.querySelector('.itemyear').textContent);
    const dateAddedB = new Date(b.querySelector('.itemyear').textContent);
    return dateAddedA - dateAddedB;
  });

  // Clear existing items
  listContainer.innerHTML = '';

  // Append sorted items
  items.forEach(item => listContainer.appendChild(item));
}

function sortByDefault() {
  // Since the items are initially in the correct order, we can simply append them back without sorting
  const items = Array.from(listContainer.querySelectorAll('.data-item'));
  listContainer.innerHTML = '';
  items.forEach(item => listContainer.appendChild(item));
}


// Add event listener for select option change
document.addEventListener('DOMContentLoaded', () => {
  const sortOptionSelect = document.getElementById('sortOption');
  sortOptionSelect.addEventListener('change', () => {
    const selectedValue = sortOptionSelect.value;
    if (selectedValue === 'name') {
      sortByName();
    } else if (selectedValue === 'dateAdded') {
      sortByDateAdded();
    }
    else if (selectedValue === 'default') {
      const itemsdf = Array.from(listContainercopy.querySelectorAll('.data-item'));
      listContainercopy.innerHTML = '';
      itemsdf.forEach(itemdf => listContainercopy.appendChild(itemdf));    }
  });

  // Initial sorting (by name)
  sortByDefault();
});