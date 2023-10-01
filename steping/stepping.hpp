
Ans VogelApproximationMethod(vector< vector<int> > costs, vector<int> supply, vector<int> demand){
    int s = costs.size();
    int d = costs[0].size();
    Ans ans(s,d);
    vector <bool> visRow (s,0), visCol (d,0);
    
    int i = 0,j = 0;
    vector< priority_queue< indexCost, vector< indexCost >, indexCostCompare > > pqRow(s);
    vector< priority_queue< indexCost, vector< indexCost >, indexCostCompare > > pqCol(d);
    for(i=0; i<s; i++){
        for(j=0; j<d; j++){
            pqRow[i].push( indexCost{j, costs[i][j]} );
            pqCol[j].push( indexCost{i, costs[i][j]} );
        }
    }
    
    vector<int> rowDiff = calcDiff(s, visRow, visCol, pqRow);
    vector<int> colDiff = calcDiff(d, visCol, visRow, pqCol);    

    int t1 = 0, t2 = 0;
    while(t1+t2 < s+d-1){
        
        // get max row difference
        int rowInd = 0, rowMax = 0;
        for(i=0; i<s; i++){
            if(rowDiff[i] > rowMax){
                rowInd = i; 
                rowMax = rowDiff[i];
            }
        }
        // get max col difference
        int colInd = 0, colMax = 0;
        for(i=0; i<d; i++){
            if(colDiff[i] > colMax){
                colInd = i; 
                colMax = colDiff[i];
            }
        }
        
        //update
        if(rowMax < colMax){
            i = pqCol[colInd].top().index;
            j = colInd;
            pqCol[colInd].pop();
        }else{
            i = rowInd;
            j = pqRow[rowInd].top().index;
            pqRow[rowInd].pop();
        }
        
        if(supply[i] <= demand[j]){
            ans.totalCost += costs[i][j] * supply[i];
            ans.allocated[i][j] = supply[i];
            demand[j] -= supply[i];
            supply[i] = 0;
            visRow[i] = 1;
            t1++;
            // update col difference for next iteration
            rowDiff[i] = -1;
            colDiff = calcDiff(d, visCol, visRow, pqCol);    
        }else{
            ans.totalCost += costs[i][j] * demand[j];
            ans.allocated[i][j] = demand[j];
            supply[i] -= demand[j];
            demand[j] = 0;
            visCol[j] = 1;
            t2++;
            // update row difference for next iteration
            colDiff[j] = -1;
            rowDiff = calcDiff(s, visRow, visCol, pqRow);      
        }
    }
    return ans;
}
 

int findLeastPathCostIndex(vector<pathCost> pathCostVector){
    int low = 0;
    int ind = 0;
    for(int i=0; i<pathCostVector.size(); i++){
        if(pathCostVector[i].cost < low){
            low = pathCostVector[i].cost;
            ind = i;
        }
    }
    return ind;
}



void updateAnsForNegativeCostClosedPath(Ans &ans, pathCost pCost){ 
    //update cost for negative least cost closed path
    int x[2];
    int y[2];
    x[0] = pCost.ind[0];
    y[0] = pCost.ind[1];
    x[1] = pCost.ind[2];
    y[1] = pCost.ind[3];
    int minAllocValue = min(ans.allocated[x[0]][y[0]], 
                    ans.allocated[x[1]][y[1]]);
        
    for(int i=0; i<2; i++){
        ans.allocated[x[i]][y[(i+1)%2]] += minAllocValue;
        ans.allocated[x[i]][y[i]] -= minAllocValue;
    }
    ans.totalCost += minAllocValue * pCost.cost;   
}

void findClosedPath(Ans ans, vector< vector<int> > costs, int s, int d, 
                    vector< vector<int> > row, vector< vector<int> > col,                   
                    vector< vector<int> > &visAllotted, int I, int pathIndex, bool &check,  // vars modified 
                    pathCost &pCost ){                                                      //output
    
    if(pathIndex == 4){
        if(checkVisitedAll(pCost, visAllotted)){  
            check = true; 
        }
        return;
    }
    if (pathIndex % 2 == 1){
        // row
        for(int i=0; i<row[I].size(); i++){
            if(ans.allocated[I][row[I][i]] and visAllotted[I][row[I][i]]==0){
                visAllotted[I][row[I][i]] = 1; 
                int temp = pCost.ind[pathIndex];
                pCost.ind[pathIndex] = row[I][i];
                findClosedPath(ans, costs, s, d, row, col, visAllotted, row[I][i], pathIndex+1, check, pCost);
                if(check == true){
                    pCost.cost -= costs[I][row[I][i]];
                    return;
                }
                visAllotted[I][row[I][i]] = 0; 
                pCost.ind[pathIndex] = temp;
            }
        }
    }else{
        //col
        for(int i=0; i<col[I].size(); i++){
            if(ans.allocated[col[I][i]][I] and visAllotted[col[I][i]][I]==0){
                visAllotted[col[I][i]][I] = 1; 
                int temp = pCost.ind[pathIndex];
                pCost.ind[pathIndex] = col[I][i];
                findClosedPath(ans, costs, s, d, row, col, visAllotted, col[I][i], pathIndex+1, check, pCost);
                if(check == true){
                    pCost.cost += costs[col[I][i]][I];
                    return;
                }
                visAllotted[col[I][i]][I] = 0; 
                pCost.ind[pathIndex] = temp;
            }
        }
    }
}

void resetVisited(vector< vector<int> > &visAllotted, vector< vector<int> > row){
    for(int i=0; i<row.size(); i++){
        for(int j=0; j<row[i].size(); j++){
            visAllotted[i][row[i][j]] = 0;
        }
    }
}

Ans SteppingStoneMethod(vector< vector<int> > costs, vector<int> supply, vector<int> demand){
    int s = costs.size();
    int d = costs[0].size();
    Ans ans = VogelApproximationMethod(costs, supply, demand);

    vector< vector<int> > row(s);
    vector< vector<int> > col(d);
    vector< vector<int> > visAllotted(s, vector<int> (d, -1));
    
    int iter = 0;
    vector<pathCost> pathCostVector;
    while(pathCostVector.size() > 0 or iter == 0){
    
        pathCostVector.clear();
        iter++;
        initVisAllotted(ans, s, d, visAllotted);  // optimize?
        initRowCol(ans, row, col, s, d);
        int temp =0;
        
        for(int i=0; i<s; i++){    
            for(int j=0; j<d; j++){
                if(ans.allocated[i][j]==0){ 
                    // reset to init state
                    resetVisited(visAllotted, row);
                    pathCost pCost;
                    pCost.ind[0] = i;
                    pCost.ind[3] = j;
                    pCost.cost = costs[i][j];
                    
                    bool check = false;
                    visAllotted[i][j] = 1;
                    findClosedPath(ans, costs, s, d, row, col, visAllotted, i, 1, check, pCost);
                    visAllotted[i][j] = -1;
                    
                    // only store negative costs
                    temp++;
                    if(pCost.cost < 0){ 
                        pathCostVector.push_back(pCost);
                    }
                }
            }
        }
        
        if (!pathCostVector.empty()){
            int ind = findLeastPathCostIndex(pathCostVector);
            updateAnsForNegativeCostClosedPath(ans, pathCostVector[ind]);
        }
    }
    return ans;
}