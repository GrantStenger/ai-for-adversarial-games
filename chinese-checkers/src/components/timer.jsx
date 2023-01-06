import "../index.css"

export default function Timer({myProps, updateMyProps}) {
    return (
        <div className="timer" >
            <p>I am TIMER</p>
            <p>{myProps.winner}</p>
        </div>
    )
}