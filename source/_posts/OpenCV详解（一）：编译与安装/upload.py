import sys
from qiniu import Auth, put_file, etag


class Uploader:
    def __init__(self, ak, sk):
        self.q = Auth(ak, sk)

    def upload_without_key(self, bn, lf):
        token = self.q.upload_token(bn, key=None)
        _ret, _info = put_file(token, None, lf)
        return _ret, _info

    def upload_with_key(self, bn, lf):
        key = etag(lf) + "".join(lf.split(".")[:-1])

    def parse_ret_info(self, r):
        return


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise ValueError

    access_key = "kFhQkJbmafdR7dZGZIuBl3peK2zJ1ozwKeNdSiUw"
    secret_key = "8Kvk_zDNJQszDT0NjOyRBnlep0w4lGXHdiUJ6OWR"
    bucket_name = "tenant-github-io"
    url = "http://qmt3iojod.hn-bkt.clouddn.com"
    uploader = Uploader(access_key, secret_key)

    for i in range(1, len(sys.argv)):
        local_file = sys.argv[i]
        ret, info = uploader.upload_without_key(bucket_name, local_file)
        assert ret['hash'] == etag(local_file)
        if ret:
            print('{0}/{1}'.format(url, ret['key']))
            
    input("Press any key to quit")
    input()
