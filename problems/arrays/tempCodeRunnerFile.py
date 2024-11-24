i, j, k = m, m+n, n
    while k >= 0:
        if nums2[k] > nums1[i]:
            nums1[j]= nums2[k] 
            j-=1
            k-=1
        elif nums2[k] < nums1[i]:
            nums1[j] = nums1[i]
            j-=1
            i-=1
        else:
            nums1[j] = nums2[k]
            j-=1
            k-=1
    return nums1