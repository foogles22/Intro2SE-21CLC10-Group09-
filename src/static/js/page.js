productsPerPage = 10; // Number of products to display per page
let currentPage = 1;

function displayProducts() {
  const productList = document.getElementById('listitem');
  const products = productList.getElementsByClassName('data-item');
  
  for (let i = 0; i < products.length; i++) {
    if (i >= (currentPage - 1) * productsPerPage && i < currentPage * productsPerPage) {
      products[i].style.display = 'block';
    } else {
      products[i].style.display = 'none';
    }
  }
}

function displayPagination() {
  const pagination = document.getElementById('pagination');
  pagination.innerHTML = '';

  const productList = document.getElementById('listitem');
  const products = productList.getElementsByClassName('data-item');
  const totalPages = Math.ceil(products.length / productsPerPage);

  const prevBtn = document.createElement('a');
  prevBtn.href = '#';
  prevBtn.textContent = '« Prev';
  prevBtn.addEventListener('click', () => {
    if (currentPage > 1) {
      currentPage--;
      displayProducts();
      displayPagination();
    }
  });
  pagination.appendChild(prevBtn);

  for (let i = 1; i <= totalPages; i++) {
    const pageLink = document.createElement('a');
    pageLink.href = '#';
    pageLink.textContent = i;

    if (i === currentPage) {
      pageLink.classList.add('active');
    }

    pageLink.addEventListener('click', () => {
      currentPage = i;
      displayProducts();
      displayPagination();
    });

    pagination.appendChild(pageLink);
  }

  const nextBtn = document.createElement('a');
  nextBtn.href = '#';
  nextBtn.textContent = 'Next »';
  nextBtn.addEventListener('click', () => {
    if (currentPage < totalPages) {
      currentPage++;
      displayProducts();
      displayPagination();
    }
  });
  pagination.appendChild(nextBtn);
}

displayProducts();
displayPagination();


