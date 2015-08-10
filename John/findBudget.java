/* Question
 * The awards committee had planned to give n research grants this year, 
 * out of a its total yearly budget. However, the budget was reduced to b dollars.
 * The committee members has decided to affect the minimal number of highest grants, 
 * by applying a maximum cap c on all grants: 
 * every grant that was planned to be higher than c will now be c dollars. 
 
 * Help the committee to choose the right value of c that would make the total sum 
 * of grants equal to the new budget.  
 
 * Given an array of grants g and a new budget b, explain and code an efficient method
 * to find the cap c. Analyze the time and space complexity of your solution.   */

// Example 
// grants = [1,2,3,4],  b = 4  ⇒  c = 1   
// grants = [1,2,3,4],  b = 7  ⇒  c = 2   
// grants = [1,2,3,4],  b = 9  ⇒  c = 3   
// grants = [1,3,4,2,1,1,1],  b = 12  ⇒  c = 3  
// grants = [1,2,0,2,4,6,8,0,23],  b = 15  ⇒  c = 2

// Solution by John Moon
public static int findCap(int[] g, int b){
  if(g.length == 0 || g == null) return -1; // 

  Arrays.sort(g); // Sort

  // accure[] is for storing summed values   
  // ex)  g = {1,2,0,2,4,6,8,0,23}
  // sorted = {0,0,1,2,2,4,6,8,23}  
  // accrue = {0,0,1,3,5,9,15,23,46} //<-- accumulated sum 
  int prev = 0; // 
  for(int i = 0; i < g.length; i++){    
    accrue[i] = g[i] + prev;    
    prev = accrue[i];
  } 
 

  if(accrue[accrue.length-1] < b) // if total sum of grants is smaller than b, 
    return g[g.length-1];         // just return the last element of g      

  int i = 0;
  while(accrue[i] <= b) i++; // find the index which accrue sum is below b   

  while(true){    
    int tmpSum = accrue[i]; // prev sum /       
    int tmpC = arr[i];  // temp c (safe candidate)       

    for(int start = i+1; start < g.length; start++){        
      tmpSum += tmpC; // iteratively add the tempC /    
    }     

    if(tmpSum <= b) return tmpC;  // check if tmpSum is smaller than b  
    else i--;  // Otherwise, decrease i, then iterate the above process again
  } 
  return -1;
}




