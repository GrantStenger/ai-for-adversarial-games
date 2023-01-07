export default function isSmallArrayInBigArray(smallArray, bigArray) {
  var currArray;
  for (let i = 0; i < bigArray.length; i++) {
    currArray = bigArray[i];
    if (currArray.length === smallArray.length) {
      var equalityCount = 0;
      for (let j = 0; j < currArray.length; j++) {
        if (smallArray[j] === currArray[j]) {
          equalityCount++;
        }
      }
      if (equalityCount == smallArray.length) return true;
    }
  }
  return false;
}
