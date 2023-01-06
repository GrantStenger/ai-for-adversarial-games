export default function isValidMove(
  gameState,
  playerID,
  startRow,
  startColumn,
  endRow,
  endColumn
) {
  if (gameState[startRow][startColumn] !== playerID) {
    // alert("Pick a spot occupied by one of your pieces.")
    return false;
  } else if (gameState[endRow][endColumn] !== 0) {
    // alert("You can only move to a spot that is unoccupied.")
    return false;
  } else if (
    startRow < 0 ||
    startRow > 8 ||
    startColumn < 0 ||
    startColumn > 8 ||
    endRow < 0 ||
    endRow > 8 ||
    endColumn < 0 ||
    endColumn > 8
  ) {
    // alert("Pick a square on the board.")
    return false;
  } else if (startRow === endRow && startColumn === endColumn) {
    // alert("You must move to another location")
    return false;
  } else if (startRow - 1 === endRow && startColumn - 1 === endColumn) {
    return true;
  } else if (startRow - 1 === endRow && startColumn === endColumn) {
    return true;
  } else if (startRow === endRow && startColumn - 1 === endColumn) {
    return true;
  } else if (startRow === endRow && startColumn + 1 === endColumn) {
    return true;
  } else if (startRow + 1 === endRow && startColumn === endColumn) {
    return true;
  } else if (startRow + 1 === endRow && startColumn + 1 === endColumn) {
    return true;
  } else if (
    startRow - 2 === endRow &&
    startColumn - 2 === endColumn &&
    gameState[startRow - 1][startColumn - 1] !== 0
  ) {
    return true;
  } else if (
    startRow - 2 === endRow &&
    startColumn === endColumn &&
    gameState[startRow - 1][startColumn] !== 0
  ) {
    return true;
  } else if (
    startRow === endRow &&
    startColumn - 2 === endColumn &&
    gameState[startRow][startColumn - 1] !== 0
  ) {
    return true;
  } else if (
    startRow === endRow &&
    startColumn + 2 === endColumn &&
    gameState[startRow][startColumn + 1] !== 0
  ) {
    return true;
  } else if (
    startRow + 2 === endRow &&
    startColumn === endColumn &&
    gameState[startRow + 1][startColumn] !== 0
  ) {
    return true;
  } else if (
    startRow + 2 === endRow &&
    startColumn + 2 === endColumn &&
    gameState[startRow + 1][startColumn + 1] !== 0
  ) {
    return true;
  }
  return false;
}
