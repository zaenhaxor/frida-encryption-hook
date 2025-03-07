console.log("bypass enc");
Java.perform(function x() {
    //hook ke SecretKeySpec, buat bikin kunci AES
    var secret_key_spec = Java.use("javax.crypto.spec.SecretKeySpec");

    //intercept constructor yg menerima byte array (kunci) sama string (algoritma)
    secret_key_spec.$init.overload("[B", "java.lang.String").implementation = function (x, y) {
        var keyString = y.toString();
        console.log("Key : b'" + keyString + "'");
        return this.$init(x, y);
    };
     //hook ke IvParameterSpec, buat nyimpen IV (Initialization Vector)
    var iv_parameter_spec = Java.use("javax.crypto.spec.IvParameterSpec");
    iv_parameter_spec.$init.overload("[B").implementation = function (x) {
        return this.$init(x);
    };
     //hook ke Cipher, ini kelas utama buat enkripsi & dekripsi
    var cipher = Java.use("javax.crypto.Cipher");
    //intercept fungsi init(), ini yg menentukan mode enkripsi/dekripsi, key dan IV
    cipher.init.overload("int", "java.security.Key", "java.security.spec.AlgorithmParameterSpec").implementation = function (x, y, z) {
        if (x == 1) {
            console.log("\nMode: encrypt");
        } else {
            console.log("\nMode: decrypt");
        }
         //mengambil data kunci aes
        var keyBytes = new Uint8Array(y.getEncoded());
        //mengambil iv yg dipakai
        var ivBytes = new Uint8Array(Java.cast(z, iv_parameter_spec).getIV());

        console.log("Key : b'" + String.fromCharCode.apply(null, keyBytes) + "'");
        console.log("IV : b'" + String.fromCharCode.apply(null, ivBytes) + "'");

        return this.init(x, y, z);
    };
     //hook ke doFinal()
    cipher.doFinal.overload("[B").implementation = function (x) {
        var dataString = String.fromCharCode.apply(null, new Uint8Array(x));
        console.log("data: b'" + dataString + "'");

        var ret = this.doFinal(x);
        return ret;
    };
});
