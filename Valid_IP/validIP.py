class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if self.isIPv4(IP):
            return "IPv4"
        elif self.isIPv6(IP):
            return "IPv6"
        else:
            return "Neither"

    def isIPv4(self, IP):
        ip_nums = IP.split(".")
        dec_digit = '0123456789'
        if len(ip_nums) != 4:
            return False

        for i in range(4):
            try:
                if int(ip_nums[i], 10) < 0 or int(ip_nums[i], 10) > 255:
                    return False
                for j in range(len(ip_nums[i])):
                    if (ip_nums[i][0] == "0" and len(ip_nums[i]) > 1) or ip_nums[i][j] not in dec_digit:
                        return False
            except:
                return False
        return True

    def isIPv6(self, IP):
        ip_nums = IP.split(":")
        hex_digit = '0123456789abcdefABCDEF'
        if len(ip_nums) != 8:
            return False

        for i in range(8):
            if len(ip_nums[i]) > 4 or len(ip_nums[i]) <= 0:
                return False
            for j in range(len(ip_nums[i])):
                if ip_nums[i][j] not in hex_digit:
                    return False

        return True
