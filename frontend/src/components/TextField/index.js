const TextField = (props) => {
    //console.log(props);
    return (
        <div>
            <label>{props.label}</label>
            <input type="text" />
        </div>
    );
};

export default TextField;