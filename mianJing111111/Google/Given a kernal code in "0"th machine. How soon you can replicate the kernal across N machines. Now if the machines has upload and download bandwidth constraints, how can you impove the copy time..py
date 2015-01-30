# encoding=utf-8
# Given a kernal code in "0"th machine. How soon you can replicate the kernal across N machines. Now if the machines has upload and download bandwidth constraints, how can you impove the copy time.
'''
I can think of three basic mechanisms for accelerating the content distribution to N nodes:
1. compression: data is compressed before transmission and decompressed before deployment. we'll need the compression factor in order to calculate its impact.
2. pipelining: intermediate nodes starts transmitting to the next machine before getting the full content. this is mainly effective when download speed is greater-equal to upload speed, so after some initial buffering period each machine transmits at the same rate it receives.
(如果文件大， 分拆成较小的部分。一个一个传)

3. sprinkling: transmit to more than one machine simultaneously. this puts an interesting trade-off, because a single transmission becomes slower, but the number of transmitting machines grows exponentially.

Let's put all this in one model:
N: number of machines, FSZ: file size in Mb, CMP: compression factor, CMPT: time to compress/decompress 1Mb, SPD: min(Upload,Download) in 1Mbps, BUF: buffering period before starting to pipeline, SPR: sprinkling factor.

SingleTransmission = (FSZ * SPR) / (SPD * CMP)
DistributionTime(N) = SingleTransmission + BUF * (LOG(N-1, SPR)-2) + 2 * CMPT

For example, if the sprinkling factor is 2, then we only need log2(N-1) copying phases. only the intermediate ones needs a buffering period, so we can ignore the first and last phases. As for compression time, we count it once for the initial file compression and once for decompressing the file at the last phase's nodes. Decompressing at the intermediate nodes does not increase the total copying time.
'''