import "../index.css"
import React, { useState } from "react"
import Spot from "./spot"
import getValidMoves from "../utils/getValidMoves"
import { useEffect } from "react"

export default function Game({myProps, updateMyProps, makeStep, makeJump, undoMove}) {

    return (
        <div className="game" style={{"--gameColor": myProps.backgroundColor}} >
            <div className="board" style={{"--boardColor": myProps.boardColor}}>
                {[...Array(9).keys()].map(i=> [...Array(9).keys()].map(j => <Spot i={i} j={j} makeStep={makeStep} makeJump={makeJump} myProps={myProps} updateMyProps={updateMyProps} />))}
            </div>
            <div className="userActions" style={{position: "absolute", right: 0, top: 0}}>
                <button onClick={undoMove}>Undo</button>
            </div>
        </div>
    )
}