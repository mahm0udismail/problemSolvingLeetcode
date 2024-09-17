class Solution {
    public String defangIPaddr(String address) {
        return address.replace(".","[.]");
        // String addressNew = "";
        // for(int i=0; i<address.length(); i++){
        //     if(address.charAt(i) == '.') {
        //         addressNew += "[.]";
        //     }
        //     else{
        //         addressNew += address.charAt(i) ;
        //     }
        // }
        // return addressNew;
    }
}