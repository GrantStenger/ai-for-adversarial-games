import "../index.css"
import aiDark from "../assets/aiDark.svg"
import aiLight from "../assets/aiLight.svg"
import man1 from "../assets/man1.svg"
import man2 from "../assets/man2.svg"
import { useEffect, useState } from "react"

export default function Timer({myProps, updateMyProps, tempTimeLeftPlayer1, tempTimeLeftPlayer2}) {
    const tempTimeLeftPlayer1String = `${String((new Date(tempTimeLeftPlayer1)).getMinutes()).padStart(2, "0")}: ${String((new Date(tempTimeLeftPlayer1)).getSeconds()).padStart(2, "0")}`
    const tempTimeLeftPlayer2String = `${String((new Date(tempTimeLeftPlayer2)).getMinutes()).padStart(2, "0")}: ${String((new Date(tempTimeLeftPlayer2)).getSeconds()).padStart(2, "0")}`
    const farProfileImg = myProps.opponentType === "computer" ? aiDark : man2
    return (
        <div className="timer" >
            {/* <div className="farTimer"><div className="indicator" state={myProps.currPlayerID === 1 ? "off" : "on"}></div><p>1:18</p></div> */}
            <div className="farTimer"><div className="indicator" state={myProps.currPlayerID === 1 ? "off" : "on"}></div><p>{tempTimeLeftPlayer2String}</p></div>
            <div className="farProfile"><figure><img src={farProfileImg} height="25px" width="25px" /></figure><p>Jeff</p></div>
            <div className="nearProfile"><figure><img src={man1} height="25px" width="25px" /></figure><p>Greg</p></div>
            {/* <div className="nearTimer"><div className="indicator" state={myProps.currPlayerID === 1 ? "on" : "off"}></div><p>2:32</p></div> */}
            <div className="nearTimer"><div className="indicator" state={myProps.currPlayerID === 1 ? "on" : "off"}></div><p>{tempTimeLeftPlayer1String}</p></div>
            <p>{(myProps.winner === 1 && "You win!") || (myProps.winner === 2 && "You lost, better luck next time") || (myProps.winner === 0 && "Game on!")}</p>
        </div>
    )
}