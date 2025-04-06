# Lin Ind Vectors

Created: 2023-06-19 06:18:47
Last Updated: 2023-06-19 06:28:12

### User - 2023-06-19 06:18:47

What makes a set of vectors linearly independent?

### Assistant - 2023-06-19 06:19:22

A set of vectors is said to be linearly independent if no vector in the set can be written as a linear combination of the others. 

Formally, if we have a set of vectors {v1, v2, ..., vn}, they are linearly independent if the only solution to the equation

a1*v1 + a2*v2 + ... + an*vn = 0

is the trivial solution where all the coefficients a1, a2, ..., an equal to zero. That is, there are no non-zero coefficients that can make the sum of these vectors equal to the zero vector. 

If there exists a non-trivial solution, i.e., if you can express any vector as a linear combination of the others with at least one non-zero coefficient, then the vectors are said to be linearly dependent. This essentially means one or more vectors in the set are "extra" or "redundant" as they can be expressed as a combination of others.

For example, consider the vectors (1,0) and (2,0) in a two-dimensional space. These are linearly dependent because you can express (2,0) as 2*(1,0). However, the vectors (1,0) and (0,1) are linearly independent, because there is no way to express one as a combination of the other.

### User - 2023-06-19 06:19:35

What is a basis?

### Assistant - 2023-06-19 06:20:06

In linear algebra, a basis of a vector space is a set of vectors that is:

1. **Linearly independent**: No vector in the set can be written as a linear combination of the others. 

2. **Spanning the space**: Any vector in the space can be written as a linear combination of the vectors in the basis.

In other words, a basis is a minimal set of vectors that allows you to express every vector in the space uniquely. 

For instance, in a two-dimensional space (or plane), a possible basis could be the vectors (1, 0) and (0, 1). Any point on the plane can be expressed as a linear combination of these two vectors. 

Similarly, in a three-dimensional space, a possible basis could be the vectors (1, 0, 0), (0, 1, 0), and (0, 0, 1). Again, any point in the space can be expressed as a linear combination of these three vectors.

It's also important to note that a basis is not unique - there are usually many different sets of vectors that can serve as a basis for a given vector space. However, the number of vectors in any basis of a particular vector space, known as the dimension of the space, is always the same.

### User - 2023-06-19 06:21:16

Give the proof that linear independence is equivalent to only having a trivial solution to the weighted sum being 0

### Assistant - 2023-06-19 06:21:48

Let's prove this in two directions: 

**Direction 1: Assuming linear independence implies only the trivial solution exists**

By definition, a set of vectors {v1, v2, ..., vn} is linearly independent if the only solution to the equation:

a1*v1 + a2*v2 + ... + an*vn = 0

is the trivial solution where all the coefficients a1, a2, ..., an are zero. This is what we are asked to prove and is an inherent property of linearly independent vectors. 

**Direction 2: Assuming only the trivial solution exists implies linear independence**

Suppose we have a set of vectors {v1, v2, ..., vn} such that the only solution to the equation:

a1*v1 + a2*v2 + ... + an*vn = 0

is the trivial solution (i.e., a1=a2=...=an=0). This means that there is no way to express any vector as a linear combination of the others (unless all coefficients are zero). Therefore, by definition, the vectors are linearly independent.

Hence, we have shown that if a set of vectors is linearly independent then the only solution to their linear combination being zero is the trivial solution, and if the only solution to their linear combination being zero is the trivial solution then the vectors are linearly independent. Thus, linear independence of vectors is equivalent to having only the trivial solution to the weighted sum being zero.


### User - 2023-06-19 06:22:49

Expand on this part of the proof: This means that there is no way to express any vector as a linear combination of the others (unless all coefficients are zero).

### Assistant - 2023-06-19 06:23:34

Sure, let's delve a bit deeper into this:

The equation a1*v1 + a2*v2 + ... + an*vn = 0 is what's known as a linear combination of vectors. The vectors are v1 through vn, and the a's are scalar coefficients. This is essentially adding together scaled versions of the vectors.

When we say this equation equals zero, we are referring to the zero vector, which in an n-dimensional space, is a vector of n zeroes.

Now, if the only solution to this equation is the trivial solution (all a's are zero), this means that there's no way for any of these vectors to add up to the zero vector unless they're all just the zero vector. They have no other way to "cancel each other out," so to speak. 

When we say "there's no way to express any vector as a linear combination of the others," what we mean is that there's no way to choose coefficients (a's) such that one of the vectors can be written as a sum of the others.

For example, if we had the vectors v1=(1, 0) and v2=(0, 1), we can't find coefficients a1 and a2 that would allow us to write v1 as a linear combination of v2, or vice versa. This is because neither vector can "contribute" to the component in which the other vector has a zero. They are orthogonal (perpendicular) to each other in a two-dimensional space.

On the other hand, if we had vectors v1=(1, 0) and v3=(2, 0), we could write v3 = 2*v1. In this case, v1 and v3 are not linearly independent because v3 can be expressed as a linear combination of v1. 

So, when all coefficients are zero, it indicates that no vector in the set can be represented as a linear combination of the others, reinforcing the fact that the vectors are linearly independent.

### User - 2023-06-19 06:25:44

Phrase this as a more proper mathematical proof. 

Assume by way of contradiction that the only solution to this equation were the trivial solution but that there exists an element vi which is a linear combination of the other elements. Then ai*vi = ... 

### Assistant - 2023-06-19 06:26:38

Sure, here is a more formal mathematical proof using contradiction:

Assume that we have a set of vectors {v1, v2, ..., vn} such that the only solution to the equation 

a1*v1 + a2*v2 + ... + an*vn = 0 

is the trivial solution where all the coefficients a1, a2, ..., an are zero.

Now, let's assume by way of contradiction that there is an element in this set, let's call it vk (where 1 <= k <= n), that can be expressed as a linear combination of the other vectors. 

That is, we can write vk = b1*v1 + b2*v2 + ... + bk-1*vk-1 + bk+1*vk+1 + ... + bn*vn for some coefficients b1, b2, ..., bn.

Now, if we substitute vk into our original equation, we get:

a1*v1 + a2*v2 + ... + ak*(b1*v1 + b2*v2 + ... + bk-1*vk-1 + bk+1*vk+1 + ... + bn*vn) + ... + an*vn = 0

which simplifies to:

(a1 + ak*b1)*v1 + (a2 + ak*b2)*v2 + ... + ak*bk-1*vk-1 + ak*bk+1*vk+1 + ... + (an + ak*bn)*vn = 0

Now, we have a contradiction. We initially stated that the only solution to the equation was the trivial solution, where all coefficients are zero. However, now we have a different set of coefficients (a1 + ak*b1, a2 + ak*b2, ..., ak*bk-1, ak*bk+1, ..., an + ak*bn), not all of which are necessarily zero (since vk is a linear combination of the other vectors), which also solves the equation.

Thus, our assumption that vk could be expressed as a linear combination of the other vectors contradicts our initial premise that the only solution to the equation was the trivial one, where all coefficients are zero. Therefore, no vector in the set can be expressed as a linear combination of the others, meaning the vectors are indeed linearly independent.

### User - 2023-06-19 06:28:12

Wouldn't a slightly more direct proof just subtract akvk from the right to get zero and assert that since vk is non-zero therefore that implies a non trivial solution?

### Assistant - 2023-06-19 06:28:57

You're right, that would indeed simplify the argument. Your approach is to subtract the term ak*vk from both sides of the equation to illustrate the contradiction directly. Let's write that out more formally:

We start with the same assumptions. We have a set of vectors {v1, v2, ..., vn} such that the only solution to the equation 

a1*v1 + a2*v2 + ... + an*vn = 0 

is the trivial solution where all the coefficients a1, a2, ..., an are zero.

Now, let's assume by way of contradiction that there is a vector vk in the set that can be expressed as a linear combination of the other vectors:

vk = b1*v1 + b2*v2 + ... + bk-1*vk-1 + bk+1*vk+1 + ... + bn*vn for some coefficients b1, b2, ..., bn.

Substitute this into our original equation to get:

a1*v1 + a2*v2 + ... + ak*(b1*v1 + b2*v2 + ... + bk-1*vk-1 + bk+1*vk+1 + ... + bn*vn) + ... + an*vn = 0

Rearrange the equation by subtracting ak*vk from both sides:

(a1 - ak*b1)*v1 + (a2 - ak*b2)*v2 + ... - ak*vk + ... + (an - ak*bn)*vn = 0

This equation contradicts our initial assumption, as it implies there is a non-trivial solution where the coefficients are not all zero (since vk can be expressed as a linear combination of the other vectors, and therefore the subtracted terms are non-zero). Therefore, our initial assumption that vk could be written as a linear combination of the other vectors must be incorrect. The vectors must be linearly independent, meaning none of them can be expressed as a linear combination of the others.


