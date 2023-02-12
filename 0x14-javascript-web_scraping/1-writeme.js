#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];

fs.writeFile(filename, 'Python is cool', 'utf-8', (error, content) => {
  if(error) {
    console.log(error);
  }else {
    console.log(content);
  }
})
