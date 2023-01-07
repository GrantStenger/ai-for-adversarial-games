import isValidJump from "./isValidJump";

export default function getValidJumps(gameState, playerID) {
  let validJumps = [];
  for (let startRow = 0; startRow < 9; startRow++) {
    for (let startColumn = 0; startColumn < 9; startColumn++) {
      for (let endRow = 0; endRow < 9; endRow++) {
        for (let endColumn = 0; endColumn < 9; endColumn++) {
          if (
            isValidJump(
              gameState,
              playerID,
              startRow,
              startColumn,
              endRow,
              endColumn
            )
          ) {
            validJumps = [
              ...validJumps,
              [startRow, startColumn, endRow, endColumn],
            ];
          }
        }
      }
    }
  }
  return validJumps;
}
