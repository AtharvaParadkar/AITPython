//Atharva Paradkar 2201144

const rectangle = {
    calculateArea: function(length, width) {
      return length * width;
    }
  };
  
  const length = 5;
  const width = 10;
  
  const area = rectangle.calculateArea(length, width);
  
  console.log('Rectangle Dimensions:');
  console.log('Length:', length);
  console.log('Width:', width);
  console.log('Area:', area);
  