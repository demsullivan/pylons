$(function() {
    if ((controller) && (action)) {
        if (window[controller]) {
            var controlObj = new window[controller]();
            if (controlObj[action])
                controlObj[action]();
        }
    }
});
	