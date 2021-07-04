function datetimeFormat(date, format) {

    date = new Date(date);
    format = format.replace(/YYYY/, date.getFullYear());
    format = format.replace(/MM/, date.getMonth() + 1);
    format = format.replace(/DD/, date.getDate());

    return format;
}

export default datetimeFormat;