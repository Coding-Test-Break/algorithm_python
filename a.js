const uploadingImgPreview = async () => {
    try {
        // logics
        for (let i = 0; i < fileInfo.length; i ++) {
            // logics
            if (i === fileInfo.length - 1) {
                reader[i].onload = (e) => {
                    let metaData = [];
                    let leng = fileInfo.length;
                    await (() => {
                        for (let i = 0; i < leng; i ++){
                            EXIF.getData(fileInfo[i], () => {
                                metaData.push(tags);
                            })
                        }    
                    })();
                    img.src = e.target.result;
                    return metaData;
                }

            } else {
                reader[i].onload = (e) => {
                    // logic
                }
            }
        }
        
    } catch (err) {
        console.log(err);
    }
}