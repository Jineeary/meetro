# Contributing to [Meetro]!😄

### Looking for the perfect meeting place? Find Meetro! 🪄🧩🚄🚅🚊

# Overview of the Project

Our mission is to help our friends easily find the most efficient subway stations and places to enjoy nearby. Whether it's a casual meeting or a special occasion, we simplify the process of choosing the perfect meeting place.

* Goal: A web service that finds a mid-point subway station for friends and recommends nearby attractions. #Effective #Convenience #Recommendation #SubwayStations #Meeting

* Target customers: People who have difficulty deciding where to meet, friends who want to meet and hang out in the middle, and people who want to choose meeting places more efficiently.

# Fixing outstanding issues

Anyone can contribute!

Answer the questions, and help me improve my documentation!

Also, spreading the news will help us a lot! 😊❤️

Applause in advance for the project that will be completed in a great way 👏👏👏

However, please check the code of conduct below and pay attention to and respect the contribution method
[Code of Conduct] (code_of_conduct link)

## Ways to contribute

There are many ways you can contribute to Transformers.

* Fix outstanding issues with the existing code.
* Submit issues related to bugs or desired new features.
* Implement new models.
* Contribute to the examples or to the documentation.

Not sure where to start? See the [first question](https://github.com/huggingface/transformers/tree/main/templates) list!

If you've solved the first problem, or you want a more challenging one, please refer to the [second problem](https://github.com/huggingface/transformers/tree/main/templates) list!

Any contribution is welcome. Every contribution is worth a lot to us! 😍

## Fix outstanding issues

Do you think there's something wrong with the existing code? Please don't [hesitate](create-a-pull-request) to create a pull request!

## Submitting a bug-related issue or feature request

Did you find a bug in our project? Please follow the instructions below to submit any bug related issues or features!

If you ask, we can answer you quickly and with a good answer.

>Bug's discovery is very helpful in completing the project

### Did you find a bug?

⚠️ Before reporting the issue, please check the following
I'd appreciate it if you could **check if it's a bug already reported**!

The problem should be related to the bug in the library itself, not the code. 

If you're not sure if the bug is in the code or in the library, please ask us first at [mail](duswlsgodqhr@naver.com )! This way we can respond faster.😎

>[!tip]
>We have a number of other [emails](email2). If you don't get an answer, please refer to it!

If you have confirmed that the bug has not been reported yet, please include the information below in the problem so that it can be resolved quickly

* Your **OS type and version** and the programming **language and version you used**

* Short, independent code snippets that can reproduce bugs (less than 30 seconds) 

* Please attach a screenshot or .txt file for any additional information that may help

To import the OS and software versions automatically, run the following command.

```bash
코드 넣기(vscode에 git연동하는 코드 넣기?)
```

### Do you want a new feature?

Have you come up with an amazing idea? Open up the issue and add it to transformer!🤓💡

Whatever the idea is, we want to listen to it! Please explain!😄


1. What's your idea?
2. Please explain the function in as much detail as possible. The more detailed it will help us understand.
3. Please show me how to use it through the code.
4. Please include the link if the feature is related to the paper.

I'll help you solve your problem! Please let me know through the [templete](https://github.com/huggingface/transformers/tree/main/templates).

## Do you want to implement a new model?

New models are constantly coming out. Do you want to give us information on new models?

*Brief description of the model and links to the paper
*If it's open source, please provide a link to the implementation
*If you have any more documents or codes that we can refer to, please provide them

Please let me know if you would like to contribute directly to the model. I'll help you add it to **transformer**!

[Technical Guide](https://github.com/huggingface/transformers/tree/main/templates) will tell you how to add a model!

## Do you want to add documentation?

We are always trying to provide more accurate and clearer documents 😖💦

Are there any typos, omissions, or unclear additions? Send us a [mail](메일주소)

Creating, building, and writing documents also helps us. See [Document](https://github.com/huggingface/transformers/tree/main/docs) for more information.

## Create a Pull Request

This is necessary to create a **Pull Request**.

1. **[Python 3.9](https://github.com/huggingface/transformers/blob/main/setup.py#L449)** or later versions
2. If there is no **vscode** you must [install](https://code.visualstudio.com/) it to access it.

* method
  
    ① Fork the [repository](https://github.com/huggingface/transformers) by
       clicking on the **[Fork](https://github.com/huggingface/transformers/fork)** button on the repository's page. This creates a copy of the code
       under your GitHub user account.
    
    ② Clone your fork to your local disk, and add the base repository as a remote:
    
       ```bash
       git clone git@github.com:<your Github handle>/transformers.git
       cd transformers
       git remote add upstream https://github.com/huggingface/transformers.git
       ```
    
    ③ Create a new branch to hold your development changes:
    
       ```bash
       git checkout -b a-descriptive-name-for-my-changes
       ```
    
       🚨 **Do not** work on the `main` branch!
    
    ④ Set up a development environment by running the following command in a virtual environment:
    
       ```bash
       pip install -e ".[dev]"
       ```
    
    ⑤ Develop the features in your branch.
    
       As you work on your code, you should make sure the test suite
       passes. Run the tests impacted by your changes like this:
    
       ```bash
       pytest tests/<TEST_TO_RUN>.py
       ```
    If you want to [test](https://huggingface.co/docs/transformers/testing), click here!
    
    🤗 Transformers relies on `black` and `ruff` to format its source code
       consistently. After you make changes, apply automatic style corrections and code verifications
       that can't be automated in one go with:
    
       ```bash
       make fixup
       ```
    
       This target is also optimized to only work with files modified by the PR you're working on.
    
       If you prefer to run the checks one after the other, the following command applies the
       style corrections:
    
       ```bash
       make style
       ```
    
       🤗 Transformers also uses `ruff` and a few custom scripts to check for coding mistakes. Quality
       controls are run by the CI, but you can run the same checks with:
    
       ```bash
       make quality
       ```
    
       Finally, we have a lot of scripts to make sure we don't forget to update
       some files when adding a new model. You can run these scripts with:
    
       ```bash
       make repo-consistency
       ```
    
       To learn more about those checks and how to fix any issues with them, check out the
       [Checks on a Pull Request](https://huggingface.co/docs/transformers/pr_checks) guide.
    
       If you're modifying documents under the `docs/source` directory, make sure the documentation can still be built. This check will also run in the CI when you open a pull request. To run a local check
       make sure you install the documentation builder:
    
       ```bash
       pip install ".[docs]"
       ```
    
       Run the following command from the root of the repository:
    
       ```bash
       doc-builder build transformers docs/source/en --build_dir ~/tmp/test-build
       ```
    
       This will build the documentation in the `~/tmp/test-build` folder where you can inspect the generated
       Markdown files with your favorite editor. You can also preview the docs on GitHub when you open a pull request.
    
       Once you're happy with your changes, add the changed files with `git add` and
       record your changes locally with `git commit`:
    
       ```bash
       git add modified_file.py
       git commit
       ```
    
       Please remember to write [good commit
       messages](https://chris.beams.io/posts/git-commit/) to clearly communicate the changes you made!
    
       To keep your copy of the code up to date with the original
       repository, rebase your branch on `upstream/branch` *before* you open a pull request or if requested by a maintainer:
    
       ```bash
       git fetch upstream
       git rebase upstream/main
       ```
    
       Push your changes to your branch:
    
       ```bash
       git push -u origin a-descriptive-name-for-my-changes
       ```
    
       If you've already opened a pull request, you'll need to force push with the `--force` flag. Otherwise, if the pull request hasn't been opened yet, you can just push your changes normally.
    
    ⑥ Now you can go to your fork of the repository on GitHub and click on **Pull Request** to open a pull request. Make sure you tick off all the boxes on our [checklist](#pull-request-checklist) below. When you're ready, you can send your changes to the project maintainers for review.
    
    ⑦ It's ok if maintainers request changes, it happens to our core contributors
       too! So everyone can see the changes in the pull request, work in your local
       branch and push the changes to your fork. They will automatically appear in
       the pull request.

### Pull request checklist

☐ Does the title Pull request summarize your contribution?

☐ If you are dealing with the issue of Pull request, please mention the issue number!

☐ Did you prefix '[ING]' before the title of the task in progress? (Prevent duplicate jobs)

☐ See **Do you want a new feature?**, **## Do you want to implement a new model?** to add a new feature

☐ Is there an informative text in the method you want to reveal?

☐ Please do not add images, videos, and other items! If you would like to forward any relevant information to us, please use [mail](duswlsgodqhr@naver.com)!

☐ Did you conduct the Pull request test?

### Tests

If you want to check the code's operation and output value, please use the [test folder](https://github.com/huggingface/transformers/tree/main/tests).

Always watch out for the **main folder**!⚠️

### Style guide

For document strings, refer to the [Document Creation Guide](https://github.com/huggingface/transformers/tree/main/docs#writing-documentation---specitication). ✍️

### Sync a forked repository with upstream main (the Hugging Face repository)

We mainly use **vscode (Visual Studio Code)**.

If possible, please proceed with fork from **vscode** to **git**!
