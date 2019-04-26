package com.luojilab.rock;

import org.apache.commons.codec.binary.Base64;

import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;


public class Crypto {

    private static byte[] SECRET_KEY = "xxx_secret_key_32byte_xxx".getBytes();

    public static String decrypt(String encrypted_text) {
        byte[] decrypted;
        try {
            Base64 base64 = new Base64(true);
            SecretKeySpec key = new SecretKeySpec(Crypto.SECRET_KEY, "AES");
            Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
            cipher.init(Cipher.DECRYPT_MODE, key);
            decrypted = cipher.doFinal(base64.decode(encrypted_text));
        } catch (Exception e) {
            return encrypted_text;
        }
        return new String(decrypted);
    }
}
