# Computer Networks Project 2 - ETH Zurich
Analyzing the border gateway protocol (BGP)’s behavior during normal times and during large-scale (global) routing events.

This is a small Project out of the Course "Computer Networks" at ETH Zurich, which I took in in my 4th semester of the Computer Science Bachelor.

## TASK

### Input File Format

Each input file is the result of running bgpdump on a RouteViews archive file. Each line in the provided files specifies a single BGP update message received by the collector. Each line consists of multiple fields associated with different fields and metadata of a BGP update message. Different fields in each line are separated by |, each of which specifying the following fields in their order of appearance:
- BGP Protocol
- timestamp (in epoch format)
- W/A/B (withdrawal/announcement/routing table)
- Peer IP (address of the monitor)
- Peer ASN (ASN of the monitor)
- Prefix
- ASPath (as a list of AS numbers separated by space) • Origin Protocol (typically always IGP)
- Next Hop
- LocalPref
- MED
- Community strings
- Atomic Aggregator
- Aggregator

### Questions

1. What is the number of all update messages?
2. What is the number of announcements?
3. What is the number of withdrawals?
4. What is the number of prefixes for which at least one BGP update is received? 
5. What is the number of prefixes for which at least one announcement is received?
6. What is the number of prefixes for which at least one withdrawals is received?
We define an update burst as the sequence of BGP update messages received for the same prefix, where the time interval between the timestamps of each two consecutive update messages in the sequence is shorter than 4 minutes. Each burst is an indicator of an event at the destination network (prefix originator). Given this definition, answer the remaning questions:
7. What is the total number of bursts?
8. What is the maximum number of bursts per prefix? 9. How long is the longest burst (in seconds)?
10. What is the average of the longest burst of all prefixes (in seconds)?
11. How many prefixes experience no bursts at all?
12. How many prefixes experience an average burst longer than 10 minutes? 13. How many prefixes experience an average burst longer than 20 minutes? 14. How many prefixes experience an average burst longer than 30 minutes?
