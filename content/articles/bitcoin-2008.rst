==============
Bitcoin (2008)
==============

:date: 2017-07-17 06:00
:category: paper reviews
:tags: bitcoin
:summary: A review of the 2008 paper titled "Bitcoin: A Peer-to-Peer
          Electronic Cash System" by Satoshi Nakamoto.
:status: published

.. contents::

Abstract
========

In this article,
I review the original 2008 Bitcoin paper
by Satoshi Nakamoto [1]_.
Jake Lerner from UC Berkeley
has also published a review [2]_.

Commentary
==========

Bitcoin has recently been in the news
because its price reached
an all-time high of about 3,000 USD per coin.
This was up from a 1-year low
of about 570 USD per coin.

.. image:: {attach}images/bitcoin-2008_coinbase.png
   :alt: Coinbase chart showing the 1-year price of Bitcoin in USD.

Google Trends shows that
the search term "bitcoin"
also reached an all-time high,
coinciding with the peak price.

.. image:: {attach}images/bitcoin-2008_google-trends.png
   :alt: Google trends showing the recent popularity of the search term
         "bitcoin".

What is Bitcoin?
Is it the digital equivalent of gold?
According to `bitcoin.org <https://bitcoin.org/en/>`_:

    Bitcoin is an innovative payment network and a new kind of money.

So from this one-line definition,
it would appear that the folks at bitcoin.org
do in fact believe that Bitcoin is money.
Is it commodity money?
Fiat money?
Or perhaps it is a new form of money?
What about the *innovative payment network*
and how does that fit in?

Let's crack open
the 2008 Bitcoin paper
and see how Nakamoto
originally presented Bitcoin
to the world!

Review
======

The People Problem
------------------

Nakamoto jumps right into the people problem:
eCommerce currently requires
both the buyer and the seller
to *trust* some 3rd-party
to process the electronic payment.
Nakamoto argues that the involvement
of a trusted 3rd-party
leads to the following problems or limitations:

* seller is impacted because non-reversible transactions are not possible
* both buyer and seller are impacted because transaction costs are higher
* both buyer and seller are impacted because microtransactions are impractical
* buyer is impacted because seller requires more information about buyer than necessary
* seller is impacted because buyer fraud exists (reversing a transaction?)

In addition to this list of problems and limitations,
I would also add the following:

* both buyer and seller are impacted because trusted 3rd-party requires more information about buyer and seller than necessary

While I do agree that these are real problems,
I would argue that the world has done quite well
with this model so far.
Sellers would prefer to have non-reversible transactions,
but due to competition,
sellers would often wish to accept reversible forms of payment,
such as credit cards.
Transaction costs are not fun,
but they are also not exorbitant.
Compared with government taxes,
transaction costs are almost negligible.
It is true that microtransactions
have yet to materialize
in this model.
However,
it is possible to buy inexpensive items
such as an iTunes song for 0.99 USD.
From my observations,
buyers and sellers are actually not concerned
with disclosing information about themselves.
And finally,
fraud has not shutdown credit card companies,
online auction sites such as eBay,
or major online merchants such as Amazon.com.

But let's keep reading,
because even though the problems
that Nakamoto identified
may not be pressing,
the existence of something like Bitcoin
could open up new opportunities to create
value for many people.

The Technical Problem
---------------------

Technical Problem #1: Transferring Physical Money
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Removing the trusted 3rd-party
would seem to require a world
where the buyer could transfer
physical money to the seller.
But this is often impractical.
First,
for small amounts of money,
the fixed shipping costs could be
impractical.
A current US postage stamp
is 0.49 USD,
which is about 50%
of the cost of a 0.99 USD iTunes song.
Second,
the time taken for payment
to reach the seller
is often on the order of
the time taken for the seller's
product to reach the buyer.
This means that if the seller
were to wait until receiving payment,
it would effectively double the total
transaction time.
This problem could be fixed by having
both the buyer and the seller
ship simultaneously,
but that exposes the seller
to the risk of buyer fraud.
Third,
sending actual physical money
exposes the buyer to both the risk of theft in transit
and the risk of seller fraud.
The risk of theft in transit
can be reduced by introducing another
trusted 3rd-party,
in this case USPS,
by converting the buyer's money into a USPS money order.
The risk of seller fraud can be reduced
by choosing buyer-vetted sellers,
which increases prices by reducing competition,
and by limiting the maximum purchase
to an amount that the buyer can afford to lose,
which increases prices by incurring opportunity costs.

From the previous paragraph,
most may conclude that it is simply
faster and safer to utilize
trusted 3rd-parties for eCommerce.

Technical Problem #2: Detecting Double Spending in Digital Money
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first technical problem
focused on a buyer
transferring *physical money*
directly to a seller.
The second technical problem
focuses on a buyer
transferring *digital money*
directly to a seller.
What would this digital money look like
and why doesn't it exist today (in 2008)?

It is possible to create
a *digital coin* (also called a digital token)
by using public key cryptography.
Here is the definition of a coin,
as expressed in Python,
using the description from the paper.

.. code:: python3
   :number-lines:

   class Coin:
       """Example of a digital coin, as described in the paper.

       NOTE: This is my own interpretation of the paper and most likely does
       not correspond with Bitcoin or any other actual cryptocurrency.
       """
       def __init__(self, first_owner_pubkey, first_owner_privkey):
           """Create a new coin, using the public and private keys of the
           original owner."""
           self.transactions = [{
               'owner_pubkey': first_owner_pubkey
               'signature': first_owner_privkey.sign(hash(first_owner_pubkey))
           }]
       def transfer(self, new_owner_pubkey, current_owner_privkey):
           """Transfer this coin to a new owner."""
           prev_transaction = self.transactions[-1]
           self.transactions.append({
               'owner_pubkey': new_owner_pubkey
               'signature': current_owner_privkey.sign(hash(prev_transaction + prev_transaction.owner_pubkey))
           })
       def verify(self):
           """Verify that this coin has a valid chain of ownership."""
           prev_transaction = None
           for transaction in self.transactions:
               if prev_transaction is None:
                   prev_transaction = transaction
                   continue
               prev_transaction.owner_pubkey.verify(transaction.signature)
               prev_transaction = transaction

A coin is a list of transactions,
where each transaction
represents the transfer of ownership
of the coin
to a new owner.
Nakamoto uses the term *transaction*,
but in this context,
it may be better to use
a term such as *transference*.
Anyone can verify that the coin
was transferred properly
by walking the list of transactions
from beginning to end,
and verifying the signature stored in each transaction
using the public key stored in the previous transaction.

With this definition
of a coin
firmly established,
Nakamoto explains
the technical problem
of *double spending*.
Double spending occurs
when an owner, Oscar,
makes a copy of his coin,
and transfers copy "A" to Alice
and copy "B" to Bob
(without telling Alice about Bob's coin
and without telling Bob about Alice's coin).
In order to prevent chaos,
it is imperative that
if double spending occurs,
that it is at least detected.
But the only way to ensure
that double spending is detected
is to observe all transactions
across all coins in the economy.
Nakamoto mentions that previous solutions
have proposed a trusted 3rd-party
to be the one
to observe and sanction all transactions.
But this proposed solution
does not solve the original problem
of seeking to avoid the use of trusted 3rd-parties.

Proposed Solution
-----------------

The proposed solution
to the problem of double spending
is really the main contribution
of this paper.
In a nutshell,
Nakamoto proposes holding all currency,
and the transactions
that record transfers of currency,
in a public database
called a *distributed timestamp service*.
This new system
solves the problem
of double spending
by making all transactions public.
For example,
Bob (and everyone) can see that
Oscar "double spent" his coin
because he previously transferred
his coin to Alice.
With such a
distributed timestamp service available,
Nakamoto notes

    For our purposes, the earliest transaction is the one that counts,
    so we don't care about later attempts to double-spend.

The remainder of this section
presents the proposed solution
by following the paper outline.

Timestamp Server
~~~~~~~~~~~~~~~~

First,
Nakamoto defines
a traditional timestamp service
that takes a block of data as input
and produces a timestamp as output.
The timestamp proves that
the block of data
*existed prior* to the creation
of the timestamp,
but does not say
*when* the block of data
was actually created
(in terms of real human time).
In fact,
the "timestamp" itself
is the output
of a hash function
and does not correspond
to real human time.
But the timestamp
can be associated
with real human time
by publishing the timestamp.
Here is the definition
of a timestamping service,
as expressed in Python,
using the description from the paper.

.. code:: python3
   :number-lines:

   class TimestampService:
      """Example of a timestamp service, as described in the paper.

      NOTE: This is my own implementation of a timestamp service and most
            likely does not correspond with any actual timestamp service.
      """
      def __init__(self):
          """Create a new (empty) timestamp service."""
          self.blockchain = []
          self.hashchain = []
      def add_block(self, block):
          """Add a new block to the blockchain."""
          self.blockchain.append(block)
          if len(self.hashchain) == 0:
              self.hashchain.append(hash(block))
          else:
              self.hashchain.append(self.hashchain[-1] + hash(block))
      def get_timestamp(self):
          """Return the most recent hash from the hashchain."""
          if len(self.hashchain) == 0:
              return None
          return self.hashchain[-1]

So how does this timestamp service
solve the double spending problem?
In my opinion,
Nakamoto is not so clear on this point.
I could imagine that blocks could contain coins.
By timestamping a block containing a coin,
one is proving that Alice is the
*first* recipient of a given coin,
and not Bob.
And from the previous section,
it is enough to prove the first recipient
in order to solve the double spending problem.

So far,
all is well.
But wait!
Who runs the timestamp service?
This traditional solution
does not work for our needs
because it requires
a trusted 3rd-party.

Proof-of-Work
~~~~~~~~~~~~~

What is proof-of-work?
Sometimes one would like to
control access to a shared resource
to prevent abuse of that resource.
Dwork and Naor (1992) [3]_
presented a scheme where
if Alice wants to access a shared resource,
she is required to "pay" for access
by performing some busywork.
Access to the resource
is then contingent
on Alice's ability
to prove that she has in fact
done this busywork.
If Alice wishes to
submit some message :math:`x`
to the shared resource,
then the busywork takes the form
of computing a *moderately hard function*
:math:`y = f(x)`.
Alice then submits
both the message
and the proof-of-work together
:math:`(x, y)`.
Principals agree not to accept messages
without valid proofs-of-work.
Bob can validate Alice's proof-of-work
by computing :math:`y' = f(x)`
and verifying that :math:`y = y'`.
As an optimization,
the moderately hard function :math:`f(x)`
can be chosen so that checking :math:`y`
is much faster than computing :math:`y`.

Nakamoto describes a particular
proof-of-work function :math:`f(x)`
that involves searching for an input :math:`x`
where the hash of that input :math:`y = f(x)`
begins with a particular number :math:`k \ge 1`
of zero bits,
which gets exponentially harder with :math:`k`.
In order to keep up with Moore's law over time,
the parameter :math:`k`
is chosen (increased?) automatically
so that a desired number of blocks
are created each hour.

Distributed Timestamp Service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In my opinion,
Nakamoto does not present
this section of the paper very clearly.
Nakamoto is describing the design
of a distributed timestamp service
where proof-of-work is required
to timestamp a block,
i.e.,
to add a block to the blockchain.
The key is that all of the principals
agree on how to verify that a block
has been timestamped correctly.
All principals possess
a complete copy of the blockchain.
Here is the definition
of a distributed timestamping service,
as expressed in Python,
using the description from the paper.

.. code:: python3
   :number-lines:

   class DistributedTimestampService:
      """Example of a distributed timestamp service, as described in the paper.

      NOTE: This is my own implementation of a distributed timestamp service
            and most likely does not correspond with any actual timestamp service.
      """
      def __init__(self, k):
          """Create a new (empty) distributed timestamp service."""
          self.k = k
          self.blockchain = []
      def add_block(self, block):
          """Add a new block to the blockchain."""
          block.prev_hash = 0
          if len(self.blockchain) > 0:
              block.prev_hash = hash(self.blockchain[-1])
          block.N = 0  # start with random number?
          while True:
              block.N += 1
              if bin(hash(block))[2:2+self.k] == 0:
                  self.blockchain.append(block)
                  break
      def verify_block(self, block):
          """Return True if a given block should be added to the blockchain
          and also add it to the blockchain."""
          prev_hash = 0
          if len(self.blockchain) > 0:
              prev_hash = hash(self.blockchain[-1])
          if block.prev_hash != prev_hash:
              return False
          if bin(hash(block))[2:2+self.k] != 0:
              return False
          self.blockchain.append(block)
          return True

So now we have
the distributed timestamp service
we mentioned
at the beginning
of this section.
The rest of this section
deals with loose ends.

Network
~~~~~~~
The paper clearly describes
the Bitcoin protocol.
Essentially,
blocks contain broadcasted transactions (coins)
and there is a great race
to extend the block chain.

Incentive
~~~~~~~~~
Why should everyone
race to extend the blockchain?
For money of course!
Each new block created
also creates a new bitcoin,
owned by the person
who created the block.
This is inflationary.
There is also a non-inflationary
incentive: transaction fees.
A transaction must specify
an input value
and an output value.
If the output value
is less than
the input value,
then the person
who creates the block
keeps the difference
for himself
as a transaction fee.

Reclaiming Disk Space
~~~~~~~~~~~~~~~~~~~~~
Not everyone needs to have
a full copy of the blockchain
in order to use Bitcoin.
Nakamoto describes
how the use of Merkle Trees
allow parts of the blockchain
to be discarded
without affecting the ability
to validate later blocks.

Simplified Payment Verification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Combined with the previous section,
anyone can verify a payment
using only a subset of the blockchain.

Combining and Splitting Value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Do we need a separate transaction
for each minimum unit of currency
(later named a satoshi after the author),
or can we have a single transaction
for a larger amount?
A transaction has one or more inputs
(coins that Alice owns)
and one or two outputs
(Alice and Bob,
where Bob is the recipient).
I felt that
this section
of the paper
was vague.

Author's Evaluation of the Proposed Solution
--------------------------------------------
Throughout the paper,
Nakamoto comments on
how such-and-such particular feature
enables some property of the system,
or prevents some problem.

On *preventing attacks*:

    We consider the scenario of an attacker trying to generate an alternate
    chain faster than the honest chain. Even if this is accomplished, it
    does not throw the system open to arbitrary changes, such as creating
    value out of thin air or taking money that never belonged to the attacker.
    Nodes are not going to accept an invalid transaction as payment, and honest
    nodes will never accept a block containing them. An attacker can only try
    to change one of his own transactions to take back money he recently spent
    ... To modify a past block, an attacker would
    have to redo the proof-of-work of the block and all blocks after it and
    then catch up with and surpass the work of the honest nodes.

Section 11 (Calculations) gives a mathematical treatment on how computationally
difficult it would be for an attacker to double spend, and presents a
theorem without proof.

On *determining representation in majority decision making*:

    The proof-of-work also solves the problem of determining representation
    in majority decision making. If the majority were based on
    one-IP-address-one-vote, it could be subverted by anyone able to
    allocate many IPs. Proof-of-work is essentially one-CPU-one-vote.
    The majority decision is represented by the longest chain, which has
    the greatest proof-of-work effort invested in it. If a majority of CPU
    power is controlled by honest nodes, the honest chain will grow the fastest
    and outpace any competing chains.

On *simultaneous broadcasts*:

    Nodes always consider the longest chain to be the correct one and will
    keep working on extending it. If two nodes broadcast different versions
    of the next block simultaneously, some nodes may receive one or the other
    first. In that case, they work on the first one they received, but save
    the other branch in case it becomes longer. The tie will be broken when the
    next proof- of-work is found and one branch becomes longer; the nodes that
    were working on the other branch will then switch to the longer one.

On *dropped broadcasts*:

    New transaction broadcasts do not necessarily need to reach all nodes.
    As long as they reach many nodes, they will get into a block before long.
    Block broadcasts are also tolerant of dropped messages. If a node does not
    receive a block, it will request it when it receives the next block and
    realizes it missed one.

On *incentives to participate*:

    By convention, the first transaction in a block is a special transaction
    that starts a new coin owned by the creator of the block. This adds an
    incentive for nodes to support the network, and provides a way to initially
    distribute coins into circulation, since there is no central authority to
    issue them.

On *incentives to stay honest*:

    The incentive may help encourage nodes to stay honest. If a greedy attacker
    is able to assemble more CPU power than all the honest nodes, he would have
    to choose between using it to defraud people by stealing back his payments,
    or using it to generate new coins. He ought to find it more profitable to
    play by the rules, such rules that favour him with more new coins than
    everyone else combined, than to undermine the system and the validity of
    his own wealth.

On *the blockchain getting too large to use*:

    A block header with no transactions would be about 80 bytes. If we suppose
    blocks are generated every 10 minutes, 80 bytes * 6 * 24 * 365 = 4.2MB per
    year. With computer systems typically selling with 2GB of RAM as of 2008,
    and Moore's Law predicting current growth of 1.2GB per year, storage should
    not be a problem even if the block headers must be kept in memory.

On *privacy*:

    ... privacy can still be maintained by breaking the flow of information
    in another place: by keeping public keys anonymous. The public can see
    that someone is sending an amount to someone else, but without information
    linking the transaction to anyone ... As an additional firewall, a new
    key pair should be used for each transaction to keep them from being
    linked to a common owner. Some linking is still unavoidable with
    multi-input transactions, which necessarily reveal that their inputs were
    owned by the same owner. The risk is that if the owner of a key is
    revealed, linking could reveal other transactions that belonged to the
    same owner.

My Analysis of the Problems, Proposed Solution, and Evaluation
--------------------------------------------------------------
I do not believe
that the people problems
identified in Bitcoin,
the paper,
are of great importance.
However,
I do believe that Bitcoin,
the system,
is making itself important
by disrupting many elements
of society and government.

The technical problems
identified in the paper
are real and well presented.

Frankly,
Nakamoto did a poor job
explaining the proposed solution.
One really has to
dig into this paper
to understand the system.

Also, Nakamoto did a poor job
analyzing the proposed solution.

Overall,
this is not a very good paper.
That said,
I would still encourage
everyone to read this paper
because there is no other
technical source for Bitcoin
that is as authoritative
as this one.
But honestly
I think one would have to
read the source code
to really understand the system.

Contributions
-------------
In my opinion,
the main contribution
of this paper
is Nakamoto's proposed solution
to the problem
of double spending,
and his evaluation
of how computationally
infeasible it is
to double spend
using his solution.
The "great race"
is an ingenious mechanism
to align the incentives
of the principals.
The second contribution
of this paper
is modeling a transaction
with multiple inputs
and two outputs.
The rest of the paper,
and the individual elements
of the proposed solution,
e.g., coins,
timestamp service,
proof-of-work,
Merkle Trees, etc.,
were published previously.

Future Directions
-----------------
Bitcoin has come a long way
since 2008,
and I don't think
that it is possible
to objectively write this section.
One could look at the original
questions and criticisms
from the 2008 to 2009
timeframe to better understand
what folks thought were the
future directions
for Bitcoin back then.

Lingering Questions
-------------------
I understand that
there is a bit of a mystery
surrounding the author,
Satoshi Nakamoto.
The conventional wisdom
is that his name
is a pseudonym.
But some folks question
whether or not
it was the work
of a single author.
I offer my own opinion
as a system researcher.
Yes,
I believe that
Satoshi Nakamoto
is a single person.
First,
my observation in life
is that the best work
tends to come from
a single creative mind,
and Bitcoin
is clearly
a very cleverly engineered system.
Second,
there are editorial deficiencies
in this paper
which would have been caught
if there had been multiple authors.
Some of the passages
are a bit awkward.
And some of the descriptions
are overly terse.
The author either has
graduate-level training,
or is one of the
very rare individuals
that can teach themselves
how to conduct research.
I would guess that
it is the latter
as it appears to me
that the paper
is copying the style and format
of academic literature
but is missing some key
traditional structures.
For example,
although there are citations,
there is no related work section.
There is also no future work section,
and there is no performance evaluation.
This paper would not have been accepted
to a top-tier conference
as it is currently written.

The paper describes how
the most common attack
would be to rewrite history
to allow an attacker
to double spend
his own coins.
To date,
has this ever
actually happened
in Bitcoin?
Would there be any
tell-tale signs
that this happened?

Should we be investing
in energy companies
and semiconductor fabs?

In the olden days of yore,
wealth was measured in cattle.
In the future,
will wealth be measured
in computational power
and access to electrical power?

Take-Away Message
-----------------
I really enjoyed reading this paper.
If I had read it back in 2008,
then I would have thought that Bitcoin
was a really well-engineered system.
It solves many different problems,
any of which would prevent Bitcoin
from being practical.
Currently Bitcoin is struggling
with scalability problems.
Years of system research
and practical experience
at companies like Google
have shown that scalability
is a very difficult property
to architect for
without the practical experience
of getting it wrong a few times.

As of mid 2017,
most of the eCommerce world continues to operate
as it did in 2008,
with VISA, MasterCard, American Express, Discover,
and a bit of PayPal for good measure.
On the other hand,
Bitcoin currently has a market cap
of about 41B USD.
Where did all of this wealth come from?
From someone's imagination.

References
==========

.. [1] Satoshi Nakamoto.
       **Bitcoin: A Peer-to-Peer Electronic Cash System.**
       2008.
       Available at: https://people.eecs.berkeley.edu/~raluca/cs261-f15/readings/bitcoin.pdf

.. [2] Jake Lerner.
       **UC Berkeley CS 261 Fall 2015 Scribe Notes: October 6: Bitcoin.**
       UC Berkeley Scribe Notes, 2015-10-08.
       Available at: https://people.eecs.berkeley.edu/~raluca/cs261-f15/scribenotes/Bitcoin.pdf

.. [3] C. Dwork and M. Naor.
       **Pricing via Processing or Combatting Junk Mail.**
       Advances in Cryptology — CRYPTO’ 92.
       Available at: http://www.weizmann.ac.il/mathusers/naor/PAPERS/pvp.pdf
