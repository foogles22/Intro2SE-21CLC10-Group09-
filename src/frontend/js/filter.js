let list = document.getElementById('list');
let filter = document.querySelector('.filter');
let count = document.getElementById('count');
let listProduct = [
    {
        id:1,
        name: 'book 1',
        author: 'author 1',
        image: 'images/menu-1.jpg',
        quantiy: 30,
        nature: {
            type: 'adult',
            language: ['vietnamese'],
            sourcetype: ['magazines']
        }
    },
    {
        id:2,
        name: 'book 2',
        author: 'author 2',
        image: 'images/menu-2.jpg',
        quantiy: 30,
        nature: {
            type: 'children',
            language: ['vietnamese'],
            sourcetype: ['academic']
        }
    },
    {
        id:3,
        name: 'book 3',
        author: 'author 1',
        image: 'images/menu-2.jpg',
        quantiy: 30,
        nature: {
            type: 'adult',
            language: ['vietnamese', 'english'],
            sourcetype: ['magazines']
        }
    },
    {
        id:4,
        name: 'book 4',
        author: 'author 2',
        image: 'images/menu-2.jpg',
        quantiy: 30,
        nature: {
            type: 'adult',
            language: ['vietnamese', 'english'],
            sourcetype: ['scholarly journals']
            //phai giong value
        }
    },
    {
        id:5,
        name: 'book 5',
        author: 'author 3',
        image: 'images/menu-1.jpg',
        quantiy: 30,
        nature: {
            type: 'adult',
            language: ['english'],
            sourcetype: ['academic']
        }
    },
    {
        id:1,
        name: 'book 6',
        author: 'author 4',
        image: 'images/menu-1.jpg',
        quantiy: 30,
        nature: {
            type: 'literature',
            language: ['vietnamese'],
            sourcetype: ['academic']
        }
    }
];

let productFilter = listProduct;
showProduct(productFilter);
function showProduct(productFilter){
    count.innerText = productFilter.length;
    list.innerHTML = '';
    productFilter.forEach(item => {
        let newItem = document.createElement('div');
        newItem.classList.add('item');

        //create image
        let newImage = new Image();
        newImage.src = item.image;
        newItem.appendChild(newImage);

        //create book name
        let newTitle = document.createElement('dvi');
        newTitle.classList.add('title');
        newTitle.innerText = item.name;
        newItem.appendChild(newTitle);

        //create author name
        let newAuthor = document.createElement('dvi');
        newAuthor.classList.add('author');
        newAuthor.innerText = item.author;
        newItem.appendChild(newAuthor);


    list.appendChild(newItem)
    });
}

filter.addEventListener('submit', function(event){
    event.preventDefault();
    let valueFilter = event.target.elements;
    productFilter = listProduct.filter(item => {
        //check category
        if(valueFilter.category.value != ''){
            if(item.nature.type != valueFilter.category.value){
                return false;
            }
        }
        //check language
        if(valueFilter.language.value != ''){
            if(!item.nature.language.includes(valueFilter.language.value)){
                return false;
            }
        }
        //check sourcetype
        if(valueFilter.sourcetype.value != ''){
            if(!item.nature.sourcetype.includes(valueFilter.sourcetype.value)){
                return false;
            }
        }

        //check book name
        if(valueFilter.bookname.value != ''){
            if(!item.name.includes(valueFilter.bookname.value)){
                return false;
            }
        }

        if(valueFilter.author.value != ''){
            if(!item.author.includes(valueFilter.author.value)){
                return false;
            }
        }
        return true;
    })
    showProduct(productFilter);
})
