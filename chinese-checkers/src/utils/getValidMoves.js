import isValidMove from "./isValidMove";

export default function getValidMoves(gameState, playerID) {
  let validMoves = [];
  for (let startRow = 0; startRow < 9; startRow++) {
    for (let startColumn = 0; startColumn < 9; startColumn++) {
      for (let endRow = 0; endRow < 9; endRow++) {
        for (let endColumn = 0; endColumn < 9; endColumn++) {
          if (
            isValidMove(
              gameState,
              playerID,
              startRow,
              startColumn,
              endRow,
              endColumn
            )
          ) {
            validMoves = [
              ...validMoves,
              [startRow, startColumn, endRow, endColumn],
            ];
          }
        }
      }
    }
  }
  return validMoves;
}
