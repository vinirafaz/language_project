import './TextField.css'

const TextField = (props) => {
    //console.log(props);
    return (
        <div>
            <label>{props.label}</label>
            <input required={props.required} type={props.type} value={props.value} onChange={props.onChange} />
        </div>
    );
};

export default TextField;