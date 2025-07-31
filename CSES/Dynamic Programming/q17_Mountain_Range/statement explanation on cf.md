 6 weeks ago, hide # |
← Rev. 2   Vote: I like it 0 Vote: I do not like it

I don't seem to understand the Mountain Range statement quite well.

Could anyone explain to me this test case from cses:
Spoiler

array: [3 46 77 16 59 32 22 41 87 89]

answer should be 7

But I think the answer should be 6: [77 16 59 32 22 41]
→ Reply

    »
    »
    -VM-
    	
    6 weeks ago, hide # ^ |
      Vote: I like it +1 Vote: I do not like it

    You can go both left and right. So the path is 89, 87, 77, 59, 41, 32,22
    → Reply
        »
        »
        »
        osmann
        	
        6 weeks ago, hide # ^ |
          Vote: I like it +1 Vote: I do not like it

        it make sense, thank you !
        → Reply
            normal_cf_user
            	
            6 weeks ago, hide # ^ |
              Vote: I like it 0 Vote: I do not like it

            why we can't jump from the last element 89 to first one 3 , as all the elements b/w them are lesser than 89 , i'm confused !
            → Reply
                osmann
                	
                6 weeks ago, hide # ^ |
                  Vote: I like it 0 Vote: I do not like it

                yes you can jump from 89 to 3, but the elements in between are not counted in the answer, only 89 and 3 are visited, after this you should look for the next jump.

                basically you can jump in any direction as long as the condition is met.

                That's what I didn't get in the beginning.
                → Reply
                    normal_cf_user
                    	
                    6 weeks ago, hide # ^ |
                      Vote: I like it 0 Vote: I do not like it

                    Got it! thanks
