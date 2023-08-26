  const table = document.getElementById('myTable');
  const pagination = document.getElementById('pagination');
  const rowsPerPage = 5; // Number of rows per page
  const visiblePages = 3; // Number of visible page links
  let currentPage = 1;

  // Function to update the table rows based on the current page
  function updateTable() {
  const rows = table.querySelectorAll('tr');
  const startIndex = (currentPage - 1) * rowsPerPage;
  const endIndex = startIndex + rowsPerPage;

  rows.forEach((row, index) => {
      if (index >= startIndex && index < endIndex) {
          row.style.display = 'table-row';
      } else {
          row.style.display = 'none';
      }
  });
  }

  // Function to generate pagination controls
  function generatePagination() {
  pagination.innerHTML = '';

  const totalRows = table.querySelectorAll('tr').length;
  const totalPages = Math.ceil(totalRows / rowsPerPage);
  const visiblePageCount = Math.min(totalPages, visiblePages);

  let startPage = currentPage - Math.floor(visiblePageCount / 2);
  if (startPage < 1) {
      startPage = 1;
  }

  const endPage = startPage + visiblePageCount - 1;
  if (endPage > totalPages) {
      startPage -= endPage - totalPages;
  }

  if (startPage > 1) {
      pagination.appendChild(createPageLink(1));
      if (startPage > 2) {
          pagination.appendChild(createEllipsis());
      }
  }
  if (currentPage != totalPages) {
    for (let i = startPage; i <= endPage; i++) {
        pagination.appendChild(createPageLink(i));
    }
  }
  else {
    for (let i = startPage; i <= endPage - 1; i++) {
        pagination.appendChild(createPageLink(i));
    }
  }
  if (endPage < totalPages) {
      if (endPage < totalPages - 1) {
          pagination.appendChild(createEllipsis());
      }
      pagination.appendChild(createPageLink(totalPages));
  }
  }

  // Function to create a page link
  function createPageLink(pageNumber) {
    const li = document.createElement('li');
    li.classList.add('page-item');
    if (pageNumber === currentPage) {
       li.classList.add('active'); // Add 'active' class to the current page button
    }
    li.innerHTML = `<a class="page-link" href="#">${pageNumber}</a>`;
 
    li.addEventListener('click', () => {
       currentPage = pageNumber;
       updateTable();
       generatePagination();
    });
 
    return li;
  }

  // Function to create an ellipsis
  function createEllipsis() {
  const li = document.createElement('li');
  li.classList.add('page-item', 'disabled');
  li.innerHTML = `<span class="page-link">...</span>`;
  return li;
  }

  // Initial setup
  updateTable();
  generatePagination();

  $(document).ready(function(){
    $("#search").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#myTable tr").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });

  });